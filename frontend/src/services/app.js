import React from 'react';
import './App.css'; // Estilos globais do app
import AnimalsGrid from './components/AnimalsGrid/AnimalsGrid'; // Importando o componente AnimalsGrid

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sistema de Gestão de Animais Exóticos</h1>
      </header>
      <main>
        <AnimalsGrid />  {/* Exibe a lista de animais */}
      </main>
    </div>
  );
}

export default App;
