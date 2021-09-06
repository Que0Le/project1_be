-- read more about the operation symbol ^! ...
-- https://nackjicholson.github.io/aiosql/defining-sql-queries.html#query-names

-- name: get-all-dictwords
SELECT *
FROM dicts;

-- name: get-dwords-by-word^
SELECT *
FROM dicts;
-- WHERE word = :word;

-- name: get-dictwords-by-word
SELECT id,
       word,
       type,
       fullword,
       content,
       created_at,
       updated_at
FROM dicts
WHERE word = :word;

-- name: get-dictword-by-id^
SELECT id,
       word,
       type,
       fullword,
       content,
       created_at,
       updated_at
FROM dicts
WHERE id = :id;

-- name: create-new-dictword<!
INSERT INTO dicts (word, type, fullword, content)
VALUES (:word, :type, :fullword, :content)
RETURNING
    id, word, type, created_at;

-- name: update-dictword-row-by-id<!
UPDATE
    dicts
SET word        = :new_word,
    type        = :new_type,
    fullword    = :new_fullword,
    content     = :new_content
WHERE id = :id
RETURNING
    id, type, word, updated_at;

-- name: delete_dictword_by_id^
DELETE
FROM dicts
WHERE id = :id
RETURNING
    id;