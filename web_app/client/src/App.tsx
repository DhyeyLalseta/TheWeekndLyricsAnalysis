import React, { useState } from "react";
import "./App.css";

const App = () => {
  const [seedText, setSeedText] = useState("");
  const [temperature, setTemperature] = useState(1);
  const [wordCount, setWordCount] = useState(15);
  const [initialText, setInitialText] = useState("");
  const [trilogyText, updateTrilogyText] = useState("");
  const [postKLText, updatePostKLText] = useState("");

  const onSubmitForm = async (e: React.FormEvent) => {
    e.preventDefault();
    setInitialText(seedText);
    try {
      console.log(seedText, temperature, wordCount);
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <>
      <body>
        <h1 className="display-4 container mt-4">The Weeknd Text Generation</h1>
        <div className="App mt-4">
          <div className="container">
            <form className="form" onSubmit={onSubmitForm}>
              <div className="form-group-row col-sm-10">
                <label className="label float-left" htmlFor="seedTextInput">
                  Seed text
                </label>
                <textarea
                  className="form-control"
                  id="seedTextInput"
                  rows={1}
                  value={seedText}
                  placeholder="what's something you wish the weeknd said... 🤔"
                  maxLength={350}
                  onChange={(e) => setSeedText(e.target.value)}
                ></textarea>
              </div>
              <div className="form-group-row col-4 mt-4">
                <label className="label float-left" htmlFor="temperatureInput">
                  Temperature{" "}
                  <small>
                    <small>(the larger the more 'creative')</small>
                  </small>
                </label>
                <input
                  className="form-control"
                  type="number"
                  id="temperatureInput"
                  value={temperature}
                  onChange={(e) => setTemperature(Number(e.target.value))}
                />
              </div>
              <div className="form-group-row col-2 mt-4">
                <label className="label float-left" htmlFor="wordCountInput">
                  Word count
                </label>
                <input
                  className="form-control"
                  type="number"
                  id="wordCountInput"
                  value={wordCount}
                  min={1}
                  max={150}
                  onChange={(e) => setWordCount(Number(e.target.value))}
                />
              </div>
              <div className="form-group-row row col-3 mt-4">
                <div className="col-sm">
                  <button className="btn btn-primary float-left" type="submit">
                    Generate
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div className="container mt-4">
          <div className="row">
            <div className="col-sm">
              <div className="card text-left">
                <div className="card-body">
                  <h5 className="card-title">
                    Trilogy-Kiss Land generated text
                  </h5>
                  <p className="card-text font-weight-light">
                    <b>{initialText}</b>{" "}
                    {trilogyText || "Waiting to generate... ⏳"}
                  </p>
                </div>
              </div>
            </div>
            <div className="col-sm">
              <div className="card text-left">
                <div className="card-body">
                  <h5 className="card-title">Post-Kiss Land generated text</h5>
                  <p className="card-text font-weight-light">
                    <b>{initialText}</b>
                    {postKLText || "Waiting to generate... ⏳"}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
};

export default App;
