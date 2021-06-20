BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,     username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'¸ù¸ðÄª±¸','mongmori@protonmail.com','010-3333-4444','https://mongmori.com','2021-06-17 12:51:21');
INSERT INTO "users" VALUES(2,'¾Æ¾ß¿ä','come@naver.com','010-2345-6789','https://www.naver.com','2021-06-17 12:51:21');
INSERT INTO "users" VALUES(3,'ÄÞÄÞ','comcom@daum.net','010-3300-4567','www.kakao.com','2021-06-17 12:50:46');
INSERT INTO "users" VALUES(4,'³Ä³Ä³Ä','nana@daum.net','010-3300-4567','www.kakao.com','2021-06-17 12:50:46');
INSERT INTO "users" VALUES(5,'Áø¶Ç¹è±â','jonddo@daum.net','010-3300-4567','www.kakao.com','2021-06-17 12:50:46');
COMMIT;
