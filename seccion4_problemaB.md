# Sección 4 — Problema B: Encuentra los errores

```tsx
function MovieList({ cinemaId }) {
    const [movies, setMovies] = useState([]);
    const [search, setSearch] = useState("");

    useEffect(() => {
        fetch(`/api/v1/cines/${cinemaId}/movies`)
            .then(res => res.json())
            .then(data => setMovies(data));
    }, []);

    const filtered = movies.filter(m =>
        m.title.toLowerCase().includes(search)
    );

    return (
        <div>
            <input
                value={search}
                onChange={e => setSearch(e.target.value)}
            />

            {filtered.map(movie => (
                <div>{movie.title} - {movie.format}</div>
            ))}
        </div>
    );
}
```

1. Falta definir el tipo de dato de cinemaId, se puede corregir creando una interface para las props del componente:

```tsx
interface MovieListProps {
    cinemaId: number;
}
```

y luego se utiliza:

```tsx
function MovieList({ cinemaId }: MovieListProps)
```

El mismo error ocurre con movies, porque se inicializa con useState([]) sin indicar qué estructura tendrán las películas, se puede definir una interface Movie y usar:
```tsx
const [movies, setMovies] = useState<Movie[]>([]);
```


2. El useEffect solo se ejecuta una vez, ya que al final tiene [], pero como el fetch depende de cinemaId, lo correcto sería que se vuelva a ejecutar cuando cambie ese valor, por lo que se puede corregir cambiando [] por [cinemaId].
```tsx
useEffect(() => {
    fetch(`/api/v1/cines/${cinemaId}/movies`)
        .then(res => res.json())
        .then(data => setMovies(data));
}, [cinemaId]);
```

3. Al filtrar por una película en específico, los títulos de las películas obtenidas en la consulta se convierten a minúsculas, pero el texto de búsqueda no, por lo que la búsqueda puede fallar por esa diferencia entre mayúsculas y minúsculas.
Se puede corregir agregando el .toLowerCase() al texto de busqueda.
```tsx
const filtered = movies.filter(m =>
    m.title.toLowerCase().includes(search.toLowerCase())
);
```

4. Al recorrer y mostrar el listado de peliculas, no se esta agregando el key para identificar cada una. Se puede corregir agregando el key
```tsx
{filtered.map(movie => (
    <div key={movie.id}>
        {movie.title} - {movie.format}
    </div>
))}
```
       