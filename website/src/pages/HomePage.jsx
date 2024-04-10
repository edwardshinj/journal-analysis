import React from "react";
import { useState } from "react";
import journal from "../assets/journal.png";

const HomePage = () => {
  const [happy, setHappy] = useState(null);
  const [sad, setSad] = useState(null);

  const submitForm = (e) => {
    e.preventDefault();
    console.log(happy + " " + sad);
  };

  return (
    <>
      <section className="bg-indigo-50">
        <div className="flex items-center justify-center">
          <h1 className="py-5 text-3xl text-center font-semibold">
            Ed's Daily Journal
          </h1>
          <img className="h-10 w-auto" src={journal} alt="journal image" />
        </div>

        <div className="container m-auto max-w-2xl py-1">
          <div className="bg-white px-6 py-6 mb-4 shadow-md rounded-md border m-4 md:m-0">
            <form onSubmit={submitForm}>
              <h2 className="text-lg text-left font-semibold mb-6">
                How was your day?
              </h2>

              <div className="mb-6">
                <label className="block mb-2 text-md font-medium text-gray-900">
                  I had HAPPY moments today.
                </label>
                <div className="flex justify-evenly">
                  {[
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree",
                  ].map((label, index) => (
                    <label
                      key={index}
                      className="flex flex-col items-center text-sm"
                    >
                      <input
                        type="radio"
                        name="question1"
                        value={index}
                        className="mb-1"
                        onChange={(e) => setHappy(e.target.value)}
                      />
                      {label}
                    </label>
                  ))}
                </div>
              </div>

              <div className="mb-6">
                <label className="block mb-2 text-md font-medium text-gray-900">
                  I had SAD moments today.
                </label>
                <div className="flex justify-evenly">
                  {[
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree",
                  ].map((label, index) => (
                    <label
                      key={index}
                      className="flex flex-col items-center text-sm"
                    >
                      <input
                        type="radio"
                        name="question2"
                        value={index}
                        className="mb-1"
                        onChange={(e) => setSad(e.target.value)}
                      />
                      {label}
                    </label>
                  ))}
                </div>
              </div>
              <button
                type="submit"
                className="mt-4 bg-rose-500 hover:bg-rose-700 text-white font-bold py-2 px-4 rounded"
              >
                Submit
              </button>
            </form>
          </div>
        </div>
      </section>
    </>
  );
};

export default HomePage;
