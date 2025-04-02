export default function divideFunction(numerator, denominator) {
  try {
    if (denominator === 0) {
      throw new Error('Cannot divide by 0');
    }
    console.log(numerator / denominator);
  } catch (e) {
    console.error(e.message);
  }
}
