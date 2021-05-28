const CryptoJS = require("crypto-js");

let rawData = CryptoJS.enc.Base64.stringify(
  "B7cKMrBgiFbPTj22+ozrjwXg9DjiF6z+9S/+Yqhfz2Q="
);

let iv = CryptoJS.enc.Utf8.parse(rawData.substring(0, 16));
let crypttext = CryptoJS.enc.Utf8.parse(rawData.substring(16));
let secret_key = "7gJkasQ89|asdTs^yb#4!2#&fJER2dpA";

// utf-8 conversion
// message = CryptoJS.enc.Utf8.parse(message);
secret_key = CryptoJS.enc.Utf8.parse(secret_key);
// iv = CryptoJS.enc.Utf8.parse(iv);

// Decrypt
var bytes = CryptoJS.AES.decrypt(crypttext.toString(), secret_key, {
  iv: iv,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7,
});
console.log(bytes.toString(CryptoJS.enc.Utf8));
