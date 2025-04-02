import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default async function handleProfileSignup(firstName, lastName, fileName) {
  // Wait for all the promise
  const results = await Promise.allSettled([
    uploadPhoto(fileName),
    signUpUser(firstName, lastName),
  ]);

    // map everything in a table and return the table
      return results.map((item) => ({
        status: item.status,
        value: item.value || item.reason,
      }));
}
