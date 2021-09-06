CREATE TABLE public.project1_dicts (
	id serial NOT NULL,
	word text NOT NULL,
	"type" text NOT NULL,
	fullword text NULL,
	"content" text NULL,
	created_at timestamptz NOT NULL DEFAULT now(),
	updated_at timestamptz NOT NULL DEFAULT now(),
	CONSTRAINT dicts_pkey_1 PRIMARY KEY (id)
);
CREATE INDEX ix_dicts_type_1 ON public.project1_dicts ("type");
CREATE INDEX ix_dicts_word_1 ON public.project1_dicts (word);



INSERT INTO public.project1_dicts (word,"type",fullword,"content")
	VALUES ('draw up the outline of a project','E-D','to draw up the outline of a project','die Grundkonzeption eines Projektes erstellen'),
		   ('do up a button','E-D','to do up a button','einen Knopf zumachen'),
		   ('do up a parcel','E-D','to do up a parcel','ein Paket fertig machen'),
		   ('do a bang-up job [coll.]','E-D','to do a bang-up job [coll.]','erstklassige Arbeit leisten'),
		   ('do up the shoelaces','E-D','to do up the shoelaces','	(sich) die Schnürsenkel (ordentlich) zubinden'),
		   ('do the drying (up)','E-D','to do the drying (up)','das Geschirr abtrocknen'),
		   ('do the washing up','E-D','to do the washing up','den Abwasch machen'),
		   ('muster (up) the courage','E-D','to muster (up) the courage to do sth.','den Mut aufbringen, etw. zu tun'),
		   ('come up with the idea','E-D','to come up with the idea to do sth.','auf den Gedanken kommen, etw. zu tun'),
		   ('get up the nerve','E-D','to get up the nerve to do sth','den Mut zusammennehmen, etw. zu tun'),
		   ('draw up a profile','E-D','to draw up a profile of the offender','ein Täterprofil erstellen'),
		   ('whip up the crowd','E-D','to whip up the crowd into a frenzy of excitement','die Menge zum Rasen bringen'),
		   ('come up to sb','E-D','to come up to sb','an jdn. herantreten (um etw. zu tun)'),
		   ('chase sb. (up) to do sth','E-D','to chase sb. (up) to do sth. [coll.]','jdm. Dampf machen, damit er / sie etw. tut [ugs.]'),
		   ('make up ones mind to do sth.','E-D','to make up ones mind to do sth.','an jdn. herantreten (um etw. zu tun)'),
		   ('make up ones mind to do sth.','E-D','to make up ones mind to do sth.','jdm. Dampf machen, damit er / sie etw. tut [ugs.]'),
		   ('be all geared up to do sth','E-D','to be all geared up to do sth. [coll.]','sich total darauf freuen, etw. zu tun [ugs.]'),
		   ('do a deal','E-D','to do a deal','ein Geschäft abschließen'),
		   ('do a service','E-D','to do a service','einen Dienst leisten'),
		   ('do a competent job','E-D','to do a competent job','gute Arbeit leisten');

INSERT INTO public.project1_dicts
(id, word, "type", fullword, "content", created_at, updated_at)
VALUES(37, 'change - dad joke', '__TYPE_STATIC_FILE', 'change_convert1bit_resize.bmp', 'i can change', '2021-09-06 17:58:37.265', '2021-09-06 17:58:37.265');

INSERT INTO public.project1_dicts
(id, word, "type", fullword, "content", created_at, updated_at)
VALUES(37, 'change - dad joke', '__TYPE_STATIC_FILE', 'change_convert1bit_resize.bmp', 'i can change', '2021-09-06 17:58:37.265', '2021-09-06 17:58:37.265');
