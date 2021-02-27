const Instagram = require('instagram-web-api')
require("dotenv").config();
const path = require("path")

const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM } = process.env; 

const client = new Instagram({ username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM })

;(async () => {
  // URL or path of photo
  const photo = path.join(__dirname,'image/teste.jpg')

  await client.login()

  // Upload Photo to feed or story, just configure 'post' to 'feed' or 'story'
  const { media } = await client.uploadPhoto({ photo: photo, caption: 'Post via Javascript', post: 'feed' })
  console.log(`https://www.instagram.com/p/${media.code}/`)
})()