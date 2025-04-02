import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  // return all the promise (uploadPhoto and createUser)
  return (
    Promise.allSettled([uploadPhoto(fileName), signUpUser(firstName, lastName)])

      // For all returned promise, log data :
      .then((results) => ({
        status: results.status,
        value: results.value || results.reason,
      })
      )
  );
}
