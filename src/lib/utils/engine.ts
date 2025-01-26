export async function search(fen: string, wtime: number, btime: number): Promise<string> {
    const params = new URLSearchParams({
        fen: fen,
        wtime: wtime.toString(),
        btime: btime.toString()
    });

    const res = await fetch(`http://localhost:8000?${params}`);
    const data = await res.text();

    return data;
}