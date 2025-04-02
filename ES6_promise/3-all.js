import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const myPromise = new Promise((resolve, reject) => {
    Promise.all([uploadPhoto(), createUser()])
      .then(([dataPhoto, dataUser]) => {
        const myReturn = `${dataPhoto.body} ${dataUser.firstName} ${dataUser.lastName}`;
        console.log(myReturn);
        return myReturn;
      })

      .catch(() => {
        reject(new Error('Signup system offline'));
      });
  });

  return myPromise;
}
