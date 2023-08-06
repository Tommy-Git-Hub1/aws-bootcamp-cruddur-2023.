INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown','Hafisadeleke97@gmail.com', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko','tadeleke1305@gmail.com', 'bayko' ,'MOCK'),
  ('Andrew Bayko','Abrown@gmail.com', 'abeezxy' ,'MOCK'),
  ('Andrew Bayko','Abayko@gmail.com', 'baykoleezy' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  );