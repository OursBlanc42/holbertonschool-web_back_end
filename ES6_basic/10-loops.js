export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];
  let idx = 0;
  for (const item of newArray) {
    newArray[idx] = appendString + item;
    idx += 1;
  }
  return newArray;
}
