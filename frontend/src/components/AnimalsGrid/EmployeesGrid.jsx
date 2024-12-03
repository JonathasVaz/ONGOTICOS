import React, { useEffect, useState } from 'react';

function EmployeesGrid() {
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/employees')
            .then(response => response.json())
            .then(data => setEmployees(data));
    }, []);

    return (
        <div>
            <h2>Funcionários da ONG</h2>
            <ul>
                {employees.map(employee => (
                    <li key={employee.id}>
                        {employee.name} - {employee.position} (Experience: {employee.experience_years} years)
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default EmployeesGrid;
