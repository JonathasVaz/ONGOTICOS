import Header from "../components/Header";
import Footer from "../components/Footer";
import AnimalsGrid from "../components/AnimalsGrid/AnimalsGrid";
import EmployeesGrid from "../components/AnimalsGrid/EmployeesGrid";

function List() {
    return (
        <>
            <Header />
            <br /><br /><br /><br />
            <AnimalsGrid />
            <EmployeesGrid />
            <Footer />
        </>
    );
}

export default List;
