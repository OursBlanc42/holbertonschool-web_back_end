export default function getListStudentsIds(obj) {
  if (typeof obj === 'object') {
    const myArray = [];
    for (let i = 0; i < obj.length; i += 1) {
      myArray.push(obj[i].id);
    }
    return myArray;
  }
  return [];
}
