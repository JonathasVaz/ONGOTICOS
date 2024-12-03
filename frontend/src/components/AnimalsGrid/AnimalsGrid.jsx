import React, { useEffect, useState } from 'react';
import AnimalHistoryGrid from './AnimalHistoryGrid';

function AnimalsGrid() {
    const [animals, setAnimals] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/animals')
            .then(response => response.json())
            .then(data => setAnimals(data));
    }, []);

    return (
        <div>
            <h2>Lista de Animais</h2>
            <ul>
                {animals.map(animal => (
                    <li key={animal.id} style={{ marginBottom: '2rem' }}>
                        <h3>{animal.name} - {animal.species}</h3>
                        <p>Idade: {animal.age} anos, Tempo de matrícula: {animal.enrollment_duration} meses</p>
                        
                        {/* Exibindo a imagem */}
                        <img
                            src={process.env.PUBLIC_URL + `/images/${animal.name.toLowerCase()}.jpg`} // Caminho relativo dentro de /public/images/
                            alt={animal.name}
                            style={{ width: '200px', height: 'auto', borderRadius: '8px' }}
                        />
                        
                        <AnimalHistoryGrid animalId={animal.id} />
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default AnimalsGrid;
