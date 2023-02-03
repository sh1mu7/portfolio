import React, { createContext, useState } from "react";

const DarkModeContext = createContext();

function DarkModeProvider(props) {

  const [darkMode, setDarkMode] = useState(false);
  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };


  return (
    <div>
      <DarkModeContext.Provider
        value={{ darkMode, toggleDarkMode, setDarkMode }}
      >
        {props.children}
      </DarkModeContext.Provider>
    </div>
  );
}

export { DarkModeProvider, DarkModeContext };
