ALTER TABLE mgn.user_message_thread_participants
DROP CONSTRAINT user_message_thread_status_pkey;

ALTER TABLE mgn.user_message_thread_participants
ADD CONSTRAINT user_message_thread_status_pkey PRIMARY KEY (
user_message_thread_participants_id,
master_user_id,
user_message_thread_id);

ALTER TABLE mgn.user_message_thread_participants
ADD CONSTRAINT user_message_thread_status_unique UNIQUE (
master_user_id,
user_message_thread_id);

---Empty message tables---
UPDATE user_message_threads set last_user_message_id=null;
DELETE FROM user_message_thread_participants;
DELETE FROM user_message_status;
DELETE FROM user_messages;
DELETE FROM user_message_threads;