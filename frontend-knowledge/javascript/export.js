// Default export (เป็นฟังก์ชันหลัก)
export default function log(message) {
  console.log(`[LOG]: ${message}`);
}

// Named export (เป็นค่าเสริม)
export const LOG_LEVEL = "DEBUG";
export function warn(message) {
  console.warn(`[WARN]: ${message}`);
}