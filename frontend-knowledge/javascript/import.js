import log, { LOG_LEVEL, warn } from './export.js';

// log ไม่ต้องใส่ {} เพราะเป็น default && เปลี่ยนชื่อเป็นอะไรก็ได้ เพราะเป็น default

log("ระบบทำงานปกติ");
warn("หน่วยความจำใกล้เต็ม");
console.log(LOG_LEVEL);