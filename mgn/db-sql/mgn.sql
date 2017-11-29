DROP SCHEMA mgn CASCADE;

CREATE SCHEMA mgn;


CREATE SEQUENCE mgn.mgn_countries_country_id_seq;

CREATE TABLE mgn.mgn_countries (
                country_id SMALLINT NOT NULL DEFAULT nextval('mgn.mgn_countries_country_id_seq'),
                short_name VARCHAR(3) UNIQUE NOT NULL,
                full_name VARCHAR(50) NOT NULL,
                isd_code VARCHAR(10) UNIQUE NOT NULL,
                states JSONB NOT NULL,
                cities JSONB NOT NULL,
                is_active SMALLINT DEFAULT 0 NOT NULL,
                CONSTRAINT mgn_countries_id_pk PRIMARY KEY (country_id)
);
COMMENT ON TABLE mgn.mgn_countries IS 'Contains all the countries name, shortcode, isd';


ALTER SEQUENCE mgn.mgn_countries_country_id_seq OWNED BY mgn.mgn_countries.country_id;

CREATE SEQUENCE mgn.like_threads_like_thread_id_seq_1;

CREATE TABLE mgn.like_threads (
                like_thread_id BIGINT NOT NULL DEFAULT nextval('mgn.like_threads_like_thread_id_seq_1'),
                like_users JSONB NOT NULL,
                updated TIMESTAMP NOT NULL,
                CONSTRAINT like_thread_id_pk PRIMARY KEY (like_thread_id)
);
COMMENT ON TABLE mgn.like_threads IS 'Contains all the like threads';


ALTER SEQUENCE mgn.like_threads_like_thread_id_seq_1 OWNED BY mgn.like_threads.like_thread_id;

CREATE SEQUENCE mgn.comment_reply_threads_comment_reply_thread_id_seq;

CREATE TABLE mgn.comment_reply_threads (
                comment_reply_thread_id BIGINT NOT NULL DEFAULT nextval('mgn.comment_reply_threads_comment_reply_thread_id_seq'),
                comment_replies JSONB NOT NULL,
                updated TIMESTAMP NOT NULL,
                CONSTRAINT comment_reply_thread_id_pk PRIMARY KEY (comment_reply_thread_id)
);
COMMENT ON TABLE mgn.comment_reply_threads IS 'Contains comment reply threads.';


ALTER SEQUENCE mgn.comment_reply_threads_comment_reply_thread_id_seq OWNED BY mgn.comment_reply_threads.comment_reply_thread_id;

CREATE SEQUENCE mgn.comment_threads_comment_thread_id_seq_1;

CREATE TABLE mgn.comment_threads (
                comment_thread_id BIGINT NOT NULL DEFAULT nextval('mgn.comment_threads_comment_thread_id_seq_1'),
                comments JSONB NOT NULL,
                comment_reply_thread_id BIGINT NOT NULL,
                updated TIMESTAMP NOT NULL,
                CONSTRAINT comment_thread_id_pk PRIMARY KEY (comment_thread_id)
);
COMMENT ON TABLE mgn.comment_threads IS 'Contains all the comments.';


ALTER SEQUENCE mgn.comment_threads_comment_thread_id_seq_1 OWNED BY mgn.comment_threads.comment_thread_id;

CREATE SEQUENCE mgn.master_gender_master_gender_id_seq_1;

CREATE TABLE mgn.master_gender (
                master_gender_id SMALLINT NOT NULL DEFAULT nextval('mgn.master_gender_master_gender_id_seq_1'),
                gender VARCHAR(10) UNIQUE NOT NULL,
                CONSTRAINT master_gender_id_pk PRIMARY KEY (master_gender_id)
);
COMMENT ON TABLE mgn.master_gender IS 'Contains all the gender details.';


ALTER SEQUENCE mgn.master_gender_master_gender_id_seq_1 OWNED BY mgn.master_gender.master_gender_id;

CREATE SEQUENCE mgn.master_language_master_language_id_seq_1;

CREATE TABLE mgn.master_language (
                master_language_id INTEGER NOT NULL DEFAULT nextval('mgn.master_language_master_language_id_seq_1'),
                language_name VARCHAR(50) UNIQUE NOT NULL,
                language_description VARCHAR(100) NOT NULL,
                is_active SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT master_language_id_pk PRIMARY KEY (master_language_id)
);
COMMENT ON TABLE mgn.master_language IS 'Contains all the languages.';


ALTER SEQUENCE mgn.master_language_master_language_id_seq_1 OWNED BY mgn.master_language.master_language_id;

CREATE SEQUENCE mgn.master_currency_master_currency_id_seq_1;

CREATE TABLE mgn.master_currency (
                master_currency_id INTEGER NOT NULL DEFAULT nextval('mgn.master_currency_master_currency_id_seq_1'),
                currency_code VARCHAR(10) UNIQUE NOT NULL,
                currency_name VARCHAR(50) NOT NULL,
                currency_description VARCHAR(100) NOT NULL,
                currency_symbol VARCHAR(30) NOT NULL,
                is_active SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT master_currency_id_pk PRIMARY KEY (master_currency_id)
);
COMMENT ON TABLE mgn.master_currency IS 'Contains all the currency.';


ALTER SEQUENCE mgn.master_currency_master_currency_id_seq_1 OWNED BY mgn.master_currency.master_currency_id;

CREATE SEQUENCE mgn.master_timezone_timezone_id_seq_1;

CREATE TABLE mgn.master_timezone (
                timezone_id INTEGER NOT NULL DEFAULT nextval('mgn.master_timezone_timezone_id_seq_1'),
                timezone_code VARCHAR(10) UNIQUE NOT NULL,
                timezone_description VARCHAR(50) NOT NULL,
                timezone_offset VARCHAR(10) NOT NULL,
                timezone_offset_dst VARCHAR(10) NOT NULL,
                is_active SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT master_timezone_id_pk PRIMARY KEY (timezone_id)
);
COMMENT ON TABLE mgn.master_timezone IS 'Contains all the timezone details.';


ALTER SEQUENCE mgn.master_timezone_timezone_id_seq_1 OWNED BY mgn.master_timezone.timezone_id;

CREATE SEQUENCE mgn.mgn_user_type_mgn_user_type_id_seq_1;

CREATE TABLE mgn.mgn_user_type (
                mgn_user_type_id SMALLINT NOT NULL DEFAULT nextval('mgn.mgn_user_type_mgn_user_type_id_seq_1'),
                user_type VARCHAR(10) UNIQUE NOT NULL,
                user_type_desc VARCHAR(30) NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT mgn_user_type_mgn_user_type_id_pk PRIMARY KEY (mgn_user_type_id)
);
COMMENT ON TABLE mgn.mgn_user_type IS 'Contains various types of MGN user.';


ALTER SEQUENCE mgn.mgn_user_type_mgn_user_type_id_seq_1 OWNED BY mgn.mgn_user_type.mgn_user_type_id;

CREATE SEQUENCE mgn.auth_type_auth_type_id_seq_1;

CREATE TABLE mgn.auth_type (
                auth_type_id SMALLINT NOT NULL DEFAULT nextval('mgn.auth_type_auth_type_id_seq_1'),
                auth_name VARCHAR(15) UNIQUE NOT NULL,
                auth_desc VARCHAR(50) NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT auth_type_auth_type_id_pk PRIMARY KEY (auth_type_id)
);
COMMENT ON TABLE mgn.auth_type IS 'Contains the various authentication type for the user.';


ALTER SEQUENCE mgn.auth_type_auth_type_id_seq_1 OWNED BY mgn.auth_type.auth_type_id;

CREATE SEQUENCE mgn.master_user_master_user_id_seq;

CREATE TABLE mgn.master_user (
                master_user_id BIGINT NOT NULL DEFAULT nextval('mgn.master_user_master_user_id_seq'),
                first_name VARCHAR(45) NOT NULL,
                last_name VARCHAR(45) NOT NULL,
                full_name VARCHAR(100) NOT NULL,
				profile_pic VARCHAR(200),
                email VARCHAR(100) UNIQUE NOT NULL,
                is_email_confirmed SMALLINT NOT NULL,
                username VARCHAR(30) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                is_active SMALLINT DEFAULT 1 NOT NULL,
                is_blocked SMALLINT DEFAULT 0 NOT NULL,
                is_deleted SMALLINT DEFAULT 0 NOT NULL,
                updated TIMESTAMP NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                auth_type_id SMALLINT NOT NULL,
                mgn_user_type_id SMALLINT NOT NULL,
                social_id VARCHAR(100),
                CONSTRAINT master_user_master_user_id_pk PRIMARY KEY (master_user_id)
);
COMMENT ON TABLE mgn.master_user IS 'Contains the authentication details of user.';


ALTER SEQUENCE mgn.master_user_master_user_id_seq OWNED BY mgn.master_user.master_user_id;

CREATE SEQUENCE mgn.user_shares_user_share_id_seq;

CREATE TABLE mgn.user_shares (
                user_share_id BIGINT NOT NULL DEFAULT nextval('mgn.user_shares_user_share_id_seq'),
                master_user_id BIGINT UNIQUE NOT NULL,
                posts JSONB NOT NULL,
                blogs JSONB NOT NULL,
                urls JSONB NOT NULL,
                updated TIMESTAMP NOT NULL,
                CONSTRAINT user_share_id_pk PRIMARY KEY (user_share_id)
);
COMMENT ON TABLE mgn.user_shares IS 'Contains all the posts, blogs, urls shared by user.';


ALTER SEQUENCE mgn.user_shares_user_share_id_seq OWNED BY mgn.user_shares.user_share_id;

CREATE SEQUENCE mgn.user_blogs_user_blog_id_seq;

CREATE TABLE mgn.user_blogs (
                user_blog_id BIGINT NOT NULL DEFAULT nextval('mgn.user_blogs_user_blog_id_seq'),
                blogger_master_user_id BIGINT NOT NULL,
                blog_name VARCHAR(200) UNIQUE NOT NULL,
                blog_subject VARCHAR(100) NOT NULL,
                blog_body VARCHAR NOT NULL,
                comment_thread_id BIGINT NOT NULL,
                like_thread_id BIGINT NOT NULL,
                visit_count INTEGER DEFAULT 0 NOT NULL,
                users_shared JSONB NOT NULL,
                updated TIMESTAMP NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_blog_id_pk PRIMARY KEY (user_blog_id)
);
COMMENT ON TABLE mgn.user_blogs IS 'Contains all the user blogs.';


ALTER SEQUENCE mgn.user_blogs_user_blog_id_seq OWNED BY mgn.user_blogs.user_blog_id;

CREATE SEQUENCE mgn.user_posts_user_post_id_seq;

CREATE TABLE mgn.user_posts (
                user_post_id BIGINT NOT NULL DEFAULT nextval('mgn.user_posts_user_post_id_seq'),
                post_text VARCHAR(200) NOT NULL,
                has_attachment SMALLINT DEFAULT 0 NOT NULL,
                attachment_url VARCHAR(200),
                comment_thread_id BIGINT NOT NULL,
                like_thread_id BIGINT NOT NULL,
                users_shared JSONB NOT NULL,
                created_by_master_user_id BIGINT NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_post_id PRIMARY KEY (user_post_id)
);
COMMENT ON TABLE mgn.user_posts IS 'Contains all the user posts.';


ALTER SEQUENCE mgn.user_posts_user_post_id_seq OWNED BY mgn.user_posts.user_post_id;

CREATE SEQUENCE mgn.user_groups_user_group_id_seq;

CREATE TABLE mgn.user_groups (
                user_group_id BIGINT NOT NULL DEFAULT nextval('mgn.user_groups_user_group_id_seq'),
                group_name VARCHAR(50) NOT NULL,
                group_description VARCHAR(200) NOT NULL,
                group_image_url VARCHAR(200),
                group_participants JSONB NOT NULL,
                admin_master_user_id BIGINT NOT NULL,
                other_admins JSONB NOT NULL,
                updated TIMESTAMP NOT NULL,
                is_active SMALLINT DEFAULT 1 NOT NULL,
                is_blocked SMALLINT DEFAULT 0 NOT NULL,
                is_deleted SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_group_id_pk PRIMARY KEY (user_group_id)
);
COMMENT ON TABLE mgn.user_groups IS 'Contains all the user groups.';


ALTER SEQUENCE mgn.user_groups_user_group_id_seq OWNED BY mgn.user_groups.user_group_id;

CREATE SEQUENCE mgn.user_messages_user_message_id_seq;

CREATE TABLE mgn.user_messages (
                user_message_id BIGINT NOT NULL DEFAULT nextval('mgn.user_messages_user_message_id_seq'),
                sent_from_master_user_id BIGINT NOT NULL,
                user_message_thread_id BIGINT NOT NULL,
                message_text VARCHAR(400) NOT NULL,
                has_attachment SMALLINT DEFAULT 0 NOT NULL,
                attachment_url VARCHAR(200),
                message_status JSONB NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_message_id_pk PRIMARY KEY (user_message_id)
);
COMMENT ON TABLE mgn.user_messages IS 'Contains all the user messages.';


ALTER SEQUENCE mgn.user_messages_user_message_id_seq OWNED BY mgn.user_messages.user_message_id;

CREATE SEQUENCE mgn.user_message_threads_user_message_thread_id_seq_2;

CREATE TABLE mgn.user_message_threads (
                user_message_thread_id BIGINT NOT NULL DEFAULT nextval('mgn.user_message_threads_user_message_thread_id_seq_2'),
                thread_creator_master_user_id BIGINT NOT NULL,
                thread_participants JSONB NOT NULL,
                last_user_message_id BIGINT NOT NULL,
                updated TIMESTAMP NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_message_thread_id_pk PRIMARY KEY (user_message_thread_id)
);
COMMENT ON TABLE mgn.user_message_threads IS 'Contains thread for messages.';


ALTER SEQUENCE mgn.user_message_threads_user_message_thread_id_seq_2 OWNED BY mgn.user_message_threads.user_message_thread_id;

CREATE SEQUENCE mgn.user_notifications_user_notification_id_seq;

CREATE TABLE mgn.user_notifications (
                user_notification_id BIGINT NOT NULL DEFAULT nextval('mgn.user_notifications_user_notification_id_seq'),
                master_user_id BIGINT UNIQUE NOT NULL,
                notifications JSONB,
                CONSTRAINT user_notification_id_pk PRIMARY KEY (user_notification_id)
);
COMMENT ON TABLE mgn.user_notifications IS 'Contains all the notifications for user.';


ALTER SEQUENCE mgn.user_notifications_user_notification_id_seq OWNED BY mgn.user_notifications.user_notification_id;

CREATE SEQUENCE mgn.user_followers_user_follower_id_seq;

CREATE TABLE mgn.user_followers (
                user_follower_id BIGINT NOT NULL DEFAULT nextval('mgn.user_followers_user_follower_id_seq'),
                follower BIGINT NOT NULL,
                following BIGINT NOT NULL,
                is_blocked SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_follower_id_pk PRIMARY KEY (user_follower_id)
);
COMMENT ON TABLE mgn.user_followers IS 'Contains users followers details.';


ALTER SEQUENCE mgn.user_followers_user_follower_id_seq OWNED BY mgn.user_followers.user_follower_id;

CREATE SEQUENCE mgn.user_connections_user_connection_id_seq;

CREATE TABLE mgn.user_connections (
                user_connection_id BIGINT NOT NULL DEFAULT nextval('mgn.user_connections_user_connection_id_seq'),
                connected_from_id BIGINT NOT NULL,
                connected_to_id BIGINT NOT NULL,
                user_message_thread_id BIGINT NOT NULL,
                is_accepted SMALLINT DEFAULT 0 NOT NULL,
                is_blocked SMALLINT DEFAULT 0 NOT NULL,
                is_ignored SMALLINT DEFAULT 0 NOT NULL,
                created TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_connections_id_pk PRIMARY KEY (user_connection_id)
);
COMMENT ON TABLE mgn.user_connections IS 'Contains user connection details.';


ALTER SEQUENCE mgn.user_connections_user_connection_id_seq OWNED BY mgn.user_connections.user_connection_id;

CREATE SEQUENCE mgn.user_profile_user_profile_id_seq;

CREATE TABLE mgn.user_profile (
                user_profile_id BIGINT NOT NULL DEFAULT nextval('mgn.user_profile_user_profile_id_seq'),
                profile_banner_image VARCHAR(200),
                dob DATE,
                master_gender_id SMALLINT NOT NULL,
                master_user_id BIGINT UNIQUE NOT NULL,
                CONSTRAINT user_profile_id_pk PRIMARY KEY (user_profile_id)
);
COMMENT ON TABLE mgn.user_profile IS 'Contains the profile details of user.';


ALTER SEQUENCE mgn.user_profile_user_profile_id_seq OWNED BY mgn.user_profile.user_profile_id;

CREATE SEQUENCE mgn.master_user_setting_master_user_setting_id_seq;

CREATE TABLE mgn.master_user_setting (
                master_user_setting_id BIGINT NOT NULL DEFAULT nextval('mgn.master_user_setting_master_user_setting_id_seq'),
                master_user_id BIGINT UNIQUE NOT NULL,
                timezone_id INTEGER NOT NULL,
                master_currency_id INTEGER NOT NULL,
                master_language_id INTEGER NOT NULL,
                CONSTRAINT master_user_setting_id_pk PRIMARY KEY (master_user_setting_id)
);
COMMENT ON TABLE mgn.master_user_setting IS 'Contains the master user settings for application.';


ALTER SEQUENCE mgn.master_user_setting_master_user_setting_id_seq OWNED BY mgn.master_user_setting.master_user_setting_id;

CREATE SEQUENCE mgn.user_access_details_user_access_details_id_seq;

CREATE TABLE mgn.user_access_details (
                user_access_details_id BIGINT NOT NULL DEFAULT nextval('mgn.user_access_details_user_access_details_id_seq'),
                master_user_id BIGINT UNIQUE NOT NULL,
                access_history JSONB,
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                city VARCHAR(50),
                state VARCHAR(50),
                zipcode VARCHAR(15),
                country_code VARCHAR(5),
                browser VARCHAR(100),
                device VARCHAR(100),
                request_string VARCHAR(150),
                platform VARCHAR(50),
                updated TIMESTAMP DEFAULT now_utc() NOT NULL,
                CONSTRAINT user_access_details_user_access_details_id PRIMARY KEY (user_access_details_id)
);
COMMENT ON TABLE mgn.user_access_details IS 'Contains the access details for the user.';


ALTER SEQUENCE mgn.user_access_details_user_access_details_id_seq OWNED BY mgn.user_access_details.user_access_details_id;

ALTER TABLE mgn.user_posts ADD CONSTRAINT like_threads_user_posts_fk
FOREIGN KEY (like_thread_id)
REFERENCES mgn.like_threads (like_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_blogs ADD CONSTRAINT like_threads_user_blogs_fk
FOREIGN KEY (like_thread_id)
REFERENCES mgn.like_threads (like_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.comment_threads ADD CONSTRAINT comment_reply_threads_comment_threads_fk
FOREIGN KEY (comment_reply_thread_id)
REFERENCES mgn.comment_reply_threads (comment_reply_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_posts ADD CONSTRAINT comment_threads_user_posts_fk
FOREIGN KEY (comment_thread_id)
REFERENCES mgn.comment_threads (comment_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_blogs ADD CONSTRAINT comment_threads_user_blogs_fk
FOREIGN KEY (comment_thread_id)
REFERENCES mgn.comment_threads (comment_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_profile ADD CONSTRAINT master_gender_user_profile_fk
FOREIGN KEY (master_gender_id)
REFERENCES mgn.master_gender (master_gender_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user_setting ADD CONSTRAINT master_language_master_user_setting_fk
FOREIGN KEY (master_language_id)
REFERENCES mgn.master_language (master_language_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user_setting ADD CONSTRAINT master_currency_master_user_setting_fk
FOREIGN KEY (master_currency_id)
REFERENCES mgn.master_currency (master_currency_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user_setting ADD CONSTRAINT master_timezone_master_user_setting_fk
FOREIGN KEY (timezone_id)
REFERENCES mgn.master_timezone (timezone_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user ADD CONSTRAINT mgn_user_type_master_user_fk
FOREIGN KEY (mgn_user_type_id)
REFERENCES mgn.mgn_user_type (mgn_user_type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user ADD CONSTRAINT auth_type_master_user_fk
FOREIGN KEY (auth_type_id)
REFERENCES mgn.auth_type (auth_type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_access_details ADD CONSTRAINT master_user_user_access_details_fk
FOREIGN KEY (master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.master_user_setting ADD CONSTRAINT master_user_master_user_setting_fk
FOREIGN KEY (master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_profile ADD CONSTRAINT master_user_user_profile_fk
FOREIGN KEY (master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_connections ADD CONSTRAINT master_user_user_connections_fk
FOREIGN KEY (connected_from_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_connections ADD CONSTRAINT master_user_user_connections_fk1
FOREIGN KEY (connected_to_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_followers ADD CONSTRAINT master_user_user_followers_fk
FOREIGN KEY (follower)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_followers ADD CONSTRAINT master_user_user_followers_fk1
FOREIGN KEY (following)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_notifications ADD CONSTRAINT master_user_user_notifications_fk
FOREIGN KEY (master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_messages ADD CONSTRAINT master_user_user_messages_fk
FOREIGN KEY (sent_from_master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_message_threads ADD CONSTRAINT master_user_user_message_threads_fk
FOREIGN KEY (thread_creator_master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_groups ADD CONSTRAINT master_user_user_groups_fk
FOREIGN KEY (admin_master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_posts ADD CONSTRAINT master_user_user_posts_fk
FOREIGN KEY (created_by_master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_blogs ADD CONSTRAINT master_user_user_blogs_fk
FOREIGN KEY (blogger_master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_shares ADD CONSTRAINT master_user_user_shares_fk
FOREIGN KEY (master_user_id)
REFERENCES mgn.master_user (master_user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_message_threads ADD CONSTRAINT user_messages_user_message_threads_fk
FOREIGN KEY (last_user_message_id)
REFERENCES mgn.user_messages (user_message_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_messages ADD CONSTRAINT user_message_threads_user_messages_fk
FOREIGN KEY (user_message_thread_id)
REFERENCES mgn.user_message_threads (user_message_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE mgn.user_connections ADD CONSTRAINT user_message_threads_user_connections_fk
FOREIGN KEY (user_message_thread_id)
REFERENCES mgn.user_message_threads (user_message_thread_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;