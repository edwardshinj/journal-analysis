import React from "react";
import { useState } from "react";
import journal from "../assets/journal.png";
import QuestionForm from "../components/QuestionForm";

const HomePage = () => {
  const [canSubmit, setCanSubmit] = useState(true);

  return (
    <section className="bg-indigo-50">
      <div className="flex items-center justify-center">
        <h1 className="py-5 text-3xl text-center font-semibold">
          Ed's Daily Journal
        </h1>
        <img className="h-10 w-auto" src={journal} alt="journal image" />
      </div>

      <div className="container m-auto max-w-2xl py-1">
        <QuestionForm />
      </div>
    </section>
  );
};

export default HomePage;
