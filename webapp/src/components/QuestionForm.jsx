import React, { useState, useEffect } from "react";
import axios from "axios";

const QuestionForm = () => {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    try {
      const response = await axios.get("/api/questions/");
      setQuestions(response.data);
      console.log(response.data);
      initializeAnswers(response.data);
    } catch {
      setError("Failed to load questions");
      console.error(err);
    }
  };

  const initializeAnswers = (questions) => {
    const initialAnswers = questions.reduce((acc, question) => {
      acc[question.id] = "";
      return acc;
    }, {});
    setAnswers(initialAnswers);
  };

  const handleChange = (questionId, value) => {
    setAnswers((prev) => ({
      ...prev,
      [questionId]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const ans = Object.keys(answers).map((key) => ({
        question_id: parseInt(key),
        choice_value: answers[key],
      }));
      console.log(ans);
      await axios.post("/api/entries/", {
        user: "1",
        choices: ans,
      });

      alert("Answers submitted successfully!");
      // Add submitted message here
    } catch (err) {
      setError("Error submitting answers");
      console.error(err);
    }
  };

  if (error) return <div>An error occurred: {error}</div>;

  return (
    <div>
      <div className="bg-white px-6 py-6 mb-4 shadow-md rounded-md border m-4 md:m-0">
        <form onSubmit={handleSubmit}>
          <h2 className="text-lg text-left font-semibold mb-6">
            How was your day?
          </h2>

          {questions.map((question) => (
            <div key={question.id} className="mb-6">
              <label className="block mb-2 text-md font-medium text-gray-900">
                {question.question_text}
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
                      name={`question-${question.id}`}
                      value={index}
                      className="mb-1"
                      onChange={(e) =>
                        handleChange(question.id, e.target.value)
                      }
                    />
                    {label}
                  </label>
                ))}
              </div>
            </div>
          ))}

          <button
            type="submit"
            className="mt-4 bg-rose-500 hover:bg-rose-700 text-white font-bold py-2 px-4 rounded"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default QuestionForm;
