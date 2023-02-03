// import { useContext } from "react";
import "./App.css";
import Container from "./Container";
import { DarkModeProvider } from "./DarkModeContext";

function App() {
  return (
    <>
    <DarkModeProvider>
      <Container />
    </DarkModeProvider>
    </>
  );
}

export default App;
