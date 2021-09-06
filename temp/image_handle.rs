use image::{/* Rgb, RgbImage,  */Luma, GrayImage};
use imageproc::drawing::draw_text_mut;
use rusttype::{Font, Scale};
use imageproc::rect::Rect;
use imageproc::drawing::{draw_filled_rect_mut, draw_line_segment_mut};
use models::user_data::UserData;
use std::fs::File;
use std::io::Write;

pub fn convert_bmp_8bit_to_1bit(input_path: String, output_path: String) {
    match std::fs::read(&input_path) {
        Ok(bytes) => {
            let mut buffer = vec![0; 48062];
            // Header bytes, copied from a 1bit bitmap photo exported by MS Paint
            let buffer_header: Vec<u8> = vec!{
                0x42, 0x4d, 0xbe, 0xbb, 
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x3e, 0x00, 
                0x00, 0x00, 0x28, 0x00,
                0x00, 0x00, 0x20, 0x03,
                0x00, 0x00, 0xe0, 0x01,
                0x00, 0x00, 0x01, 0x00,
                0x01, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x80, 0xbb,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0xff, 0xff,
                0xff, 0x00
            };

            // Copy header to output buffer
            buffer[..62].clone_from_slice(&buffer_header[..62]);

            // Now encode 8 bytes into 1 single byte
            for i in 0..48000 {
                let mut value: u8 = 0;
                /**/
                if bytes[1078 + i*8] > 2^7 {
                    value |= 0b1000_0000;
                } else {
                    value &= 0b0111_1111;
                }
                /**/
                if bytes[1078 + i*8+1] > 2^7 {
                    value |= 0b0100_0000;
                } else {
                    value &= 0b1011_1111;
                }
                /**/
                if bytes[1078 + i*8+2] > 2^7 {
                    value |= 0b0010_0000;
                } else {
                    value &= 0b1101_1111;
                }
                /**/
                if bytes[1078 + i*8+3] > 2^7 {
                    value |= 0b0001_0000;
                } else {
                    value &= 0b1110_1111;
                }
                /**/
                if bytes[1078 + i*8+4] > 2^7 {
                    value |= 0b0000_1000;
                } else {
                    value &= 0b1111_0111;
                }
                /**/
                if bytes[1078 + i*8+5] > 2^7 {
                    value |= 0b0000_0100;
                } else {
                    value &= 0b1111_1011;
                }
                /**/
                if bytes[1078 + i*8+6] > 2^7 {
                    value |= 0b0000_0010;
                } else {
                    value &= 0b1111_1101;
                }
                /**/
                if bytes[1078 + i*8+7] > 2^7 {
                    value |= 0b0000_0001;
                } else {
                    value &= 0b1111_1110;
                }
                buffer[62 + i] = value;
            }
            // Create output file
            let mut f = File::create(output_path).expect("Unable to create file");
            f.write_all(&buffer).expect("Unable to write data");
        }
        Err(e) => {
            if e.kind() == std::io::ErrorKind::PermissionDenied {
                eprintln!("please run again with appropriate permissions.");
                return;
            }
            panic!("{}", e);
        }
    }
}

pub fn create_bitmap_from_user_data(ud: UserData, name: String) -> String {
    let mut image = GrayImage::new(800, 480);
    let bm_white = Luma([255u8]);
    let bm_black = Luma([0u8]);
    let font = Vec::from(include_bytes!("ARIAL.TTF") as &[u8]);
    let font = Font::try_from_vec(font).unwrap();

    let height = 12.4;

    // White background
    draw_filled_rect_mut(
        &mut image, 
        Rect::at(0, 0).of_size(800, 480), 
        bm_white
    );
    
    // Title and the separate line
    draw_text_mut(
        &mut image, bm_black, 10, 10, 
        Scale{x: height * 4.5, y: height*4.5}, 
        &font, &ud.title
    );
    draw_line_segment_mut(
        &mut image, 
        (0f32, 67f32), (800f32, 67f32), 
        bm_black
    );

    // Content
    let body: String = ud.content.clone().replace("\n", " ").replace("\t", " ");
    let mut pos: usize = 0;
    let char_per_line: usize = 40;
    for n in 1..10 {
        //println!("{} ###", pos);
        let mut _temp: String;
        if pos<(body.len() + char_per_line -1) {
            _temp = body.chars().skip(pos).take(pos+char_per_line).collect();
            pos += char_per_line;
            draw_text_mut(
                &mut image, bm_black, 5, 65+n*30, 
                Scale{x: height * 3.5, y: height*3.5}, &font, &_temp
            );
            //println!("{} ###", _temp);
            //println!("-----------------------------");
        } else if pos>=(body.len() + char_per_line) {
            _temp = body.chars().skip(pos).take(body.len()-1).collect();
            draw_text_mut(
                &mut image, bm_black, 5, 65+n*30, 
                Scale{x: height * 3.0, y: height*3.0}, &font, &_temp
            );
            //println!("{} ###", _temp);
            break;
        }
    }

    // Note and the separate line
    draw_line_segment_mut(
        &mut image, (0f32, 400f32), 
        (800f32, 400f32), bm_black
    );
    draw_text_mut(
        &mut image, bm_black, 5, 410, 
        Scale{x: height * 3.0, y: height*3.0}, 
        &font, &ud.note
    );

    let filepath_8bit: String = "public/next/".to_string() + &name + "_8bit.bmp";
    let filepath_1bit: String = "public/next/".to_string() + &name + "_1bit.bmp";
    let _ = image.save(&filepath_8bit).unwrap();

    /* Convert to 1bit. Note that in output file, 1 byte holds infor for 8 pixels */
    convert_bmp_8bit_to_1bit(filepath_8bit, filepath_1bit.clone());

    filepath_1bit
}