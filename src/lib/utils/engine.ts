export async function search(fen: string, wtime: number, btime: number, move: string): Promise<string> {
    const params = new URLSearchParams({
        fen: fen,
        wtime: wtime.toString(),
        btime: btime.toString(),
        move: move
    });

    const res = await fetch(`http://localhost:8000?${params}`, {
        method: 'GET'
    });
    const data = await res.text();
    // console.log(`Bot plays ${data}`);

    return data;
}