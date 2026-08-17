import { useEffect, useState } from "react";


interface WeekSelectorProps {
    year: number;
    onWeekSelect: (idWeek: number) => void;
}


interface Week {
    id_week: number;
    week_number: number;
    init_date: string;
    end_date: string;
    movies_count: number;
}


interface WeeksResponse {
    data: Week[];
}


function formatDate(date: string) {
    return new Date(date).toLocaleDateString("es-MX", {
        day: "2-digit",
        month: "short",
        timeZone: "UTC"
    });
}


function WeekSelector({ year, onWeekSelect }: WeekSelectorProps) {
    const [weeks, setWeeks] = useState<Week[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const controller = new AbortController();

        fetch(`/api/v1/weeks?year=${year}&status=assigned`, {
            signal: controller.signal
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Error al cargar semanas");
                }

                return response.json() as Promise<WeeksResponse>;
            })
            .then((data) => {
                setWeeks(data.data);
            })
            .catch((err) => {
                if (err.name !== "AbortError") {
                    setError(true);
                }
            })
            .finally(() => {
                if (!controller.signal.aborted) {
                    setLoading(false);
                }
            });

        return () => {
            controller.abort();
        };
    }, [year]);

    if (loading) {
        return <p>Cargando...</p>;
    }

    if (error) {
        return <p>Error al cargar semanas</p>;
    }

    return (
        <select
            defaultValue=""
            onChange={(e) => onWeekSelect(Number(e.target.value))}
        >
            <option value="" disabled>
                Selecciona una semana
            </option>

            {weeks.map((week) => (
                <option key={week.id_week} value={week.id_week}>
                    Semana {week.week_number} ({formatDate(week.init_date)} - {formatDate(week.end_date)})
                </option>
            ))}
        </select>
    );
}


export default WeekSelector;