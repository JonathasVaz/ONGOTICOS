import React, { useEffect, useState } from 'react';

function AnimalHistoryGrid({ animalId }) {
    const [history, setHistory] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:5000/api/animal_history/${animalId}`)
            .then(response => response.json())
            .then(data => setHistory(data));
    }, [animalId]);

    if (!history) return <p>Loading history...</p>;

    return (
        <div>
            <h3>History of Animal {animalId}</h3>
            <p>{history.history}</p>
        </div>
    );
}

export default AnimalHistoryGrid;
