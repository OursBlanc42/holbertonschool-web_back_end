process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (userInput) => {
  console.log(`Your name is ${userInput.toString().trim()}`);
  console.log('This important software is now closing');
  process.exit();
});
