import WebSocket from 'ws';

export class Engine {
    private latest: string;
    private ws: WebSocket

    public constructor() {
        this.latest = "";
        this.ws = new WebSocket('ws://localhost:8765');

        this.ws.on('message', (message: string) => {
            console.log(`Received message from server: ${message}`);
            this.latest = message;
        });
    }

    private async getResponse(msg: string, duration: number): Promise<string> {
        this.ws.send(msg);

        const resp = new Promise<string>((resolve) => {
            setTimeout(() => {
                if (this.latest == "")
                    throw new Error(`Failed to get response from ${msg} after ${duration}ms.`);
    
                resolve(this.latest);
            }, duration * 1000)
        })
        return await resp;
    }

    public async search(fen: string, wtime: number, btime: number): Promise<string> {
        const move = await this.getResponse(`search ${fen} ${wtime} ${btime}`, 3);
        return move;
    }
}