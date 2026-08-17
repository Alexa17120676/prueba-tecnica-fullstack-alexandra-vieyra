import WeekSelector from "./WeekSelector";

function App() {
    const handleWeekSelect = (idWeek: number) => {
        console.log("Semana seleccionada:", idWeek);
    };

    return (
        <div>
            <h1>Selector de semanas</h1>

            <WeekSelector
                year={2026}
                onWeekSelect={handleWeekSelect}
            />
        </div>
    );
}

export default App;