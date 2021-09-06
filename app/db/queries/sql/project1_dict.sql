-- read more about the operation symbol ^! ...
-- https://nackjicholson.github.io/aiosql/defining-sql-queries.html#query-names

-- name: p1-get-all-dictwords
SELECT *
FROM project1_dicts;

-- name: p1-get-dwords-by-word^
SELECT *
FROM project1_dicts;

-- name: p1-get-1-random-dictword^
SELECT *
FROM project1_dicts
ORDER BY random() limit 1;

-- name: p1-get-dictwords-by-word
SELECT id,
       word,
       type,
       fullword,
       content,
       created_at,
       updated_at
FROM project1_dicts
WHERE word = :word;

-- name: p1-get-dictword-by-id^
SELECT id,
       word,
       type,
       fullword,
       content,
       created_at,
       updated_at
FROM project1_dicts
WHERE id = :id;

-- name: p1-create-new-dictword<!
INSERT INTO project1_dicts (word, type, fullword, content)
VALUES (:word, :type, :fullword, :content)
RETURNING
    id, word, type, created_at;

-- name: p1-update-dictword-row-by-id<!
UPDATE
    project1_dicts
SET word        = :new_word,
    type        = :new_type,
    fullword    = :new_fullword,
    content     = :new_content
WHERE id = :id
RETURNING
    id, type, word, updated_at;

-- name: p1-delete_dictword_by_id^
DELETE
FROM project1_dicts
WHERE id = :id
RETURNING
    id;