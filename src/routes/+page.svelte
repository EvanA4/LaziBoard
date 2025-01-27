<script lang="ts">
    import { search } from '$lib/utils/engine';
    import { Chess } from 'svelte-chess';
    import '$lib/chessStyle.css';
	import { onMount } from 'svelte';
	import type { Color } from 'chess.js';
    import { timerString } from '$lib/utils/timef';

    import PauseImg from '$lib/assets/svgs/pause.svelte';
    import PlayImg from '$lib/assets/svgs/play.svelte';
    import RestartImg from '$lib/assets/svgs/restart.svelte';
    import SetTimer from '$lib/components/SetTimer.svelte';


    let bstart = $state<number>(300);
    let wstart = $state<number>(300);

    let isGameOver = $state<number>(0);
    let turn = $state<Color | undefined>();
    // let fen = $state<string>("r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4"); // to test game over
    let fen = $state<string>("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    let started = $state<boolean>(false);
    let paused = $state<boolean>(false);
    let playerTeam = $state<string>("w");

    let bsec = $state<number>(300);
    let wsec = $state<number>(300);

    let timerInterval: ReturnType<typeof setInterval>;
    let chess: any;

    onMount(() => {
        timerInterval = setInterval(() => {
            if (started && !paused && !isGameOver) {
                if (turn == "b") {
                    bsec -= .1;

                    if (bsec < 0) {
                        bsec = 0;
                        isGameOver = 2;
                    }
                }

                else {
                    wsec -=.1;

                    if (wsec < 0) {
                        wsec = 0;
                        isGameOver = 2;
                    }
                }

            }
        }, 100)
    })

    async function moveListener(event: any) {
        // console.log(turn, playerTeam);

        // check if bot needs to play
        if (playerTeam == turn) {
            // console.log("I'm running!");
            const move = event.detail;
            let newmove = await search(fen, wsec, bsec, move.san);
            chess.move(newmove);
        }

        // const move = event.detail;
        // console.log( `${move.color} played ${move.san}` );
    }

    async function startGame() {
        started = true;
        // console.log(turn, playerTeam);

        // check if bot needs to play
        if (playerTeam != turn) {
            // console.log("I'm running at start!");
            let newmove = await search(fen, wsec, bsec, "");
            chess.move(newmove);
        }
    }

    function gameOverListener(event: any) {
        isGameOver = 1;
    }

    function getWinner(turn: Color | undefined, isGameOver: number) {
        if (turn == "w") return "Black";
        return "White";
    }

    function resetGame() {
        chess.reset();
        isGameOver = 0;
        started = false;
        paused = false;
        bsec = 300;
        wsec = 300;
    }

    function changeTeams() {
        chess.toggleOrientation();
        if (playerTeam == "w") playerTeam = "b";
        else playerTeam = "w";
    }
</script>

<div class="flex flex-col items-center justify-center h-[100vh]">
    <div class="w-[100vw] flex justify-center">
        <div class="w-[90vh] relative">


            {#if isGameOver || !started}
                <div class="absolute top-0 left-0 w-[100%] h-[100%] bg-black bg-opacity-80 z-10 flex flex-col items-center justify-center">
                    {#if isGameOver}
                        <p class="text-white text-3xl">{getWinner(turn, isGameOver)} wins!</p>
                        <button onclick={resetGame} class="px-5 py-2 rounded-lg mt-5 bg-blue-600 hover:bg-blue-500 text-white">Reset</button>
                    {:else}
                        <div>
                            <p class="text-white text-[30px] text-center">Play as <b>{playerTeam == "w" ? "White" : "Black"}</b></p>
                            <div>
                                <button onclick={startGame} class="px-5 py-2 rounded-lg mt-5 bg-green-600 hover:bg-green-500 text-white">Start</button>
                                <button onclick={changeTeams} class="px-5 py-2 rounded-lg mt-5 bg-blue-600 hover:bg-blue-500 text-white">Change Teams</button>
                            </div>
                        </div>
                    {/if}
                </div>

                <div class="absolute bottom-[10%] left-[25%] -translate-x-[50%] z-10">
                    <SetTimer bind:startTime={bstart}/>
                </div>

                <div class="absolute bottom-[10%] left-[75%] -translate-x-[50%] z-10">
                    <SetTimer bind:startTime={wstart}/>
                </div>
            {/if}

            {#if paused || playerTeam != turn}
                <div class="absolute top-0 left-0 w-[100%] h-[100%] z-10"></div>
            {/if}

            <Chess class="cg-paper" on:move={moveListener} on:gameOver={gameOverListener} bind:this={chess} bind:turn={turn} bind:fen={fen}/>
                
        
        </div>


        <div class="bg-neutral-900 h-[90vh] flex flex-col justify-between items-center w-[200px] py-10">
            <p class="text-white text-[40px]">{timerString(playerTeam == "w" ? bsec : wsec)}</p>

            <div class="flex flex-col items-center gap-5">
                <button onclick={() => paused = !paused} class="opacity-70 hover:opacity-100">
                    {#if paused}
                        <PlayImg />
                    {:else}    
                        <PauseImg />
                    {/if}
                </button>
                {#if started && !isGameOver}
                    <button onclick={resetGame} class="px-5 py-2 rounded-lg mt-5 opacity-70 hover:opacity-100 text-white hover:animate-spin">
                        <RestartImg />
                    </button>
                {/if}
            </div>

            <p class="text-white text-[40px]">{timerString(playerTeam == "w" ? wsec : bsec)}</p>
        </div>
    </div>
</div>