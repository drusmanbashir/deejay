BEGIN;
ALTER TABLE "blog_post" DROP CONSTRAINT "category_id_refs_id_1c210c34";
DROP TABLE "blog_category";
DROP TABLE "blog_post";

COMMIT;
