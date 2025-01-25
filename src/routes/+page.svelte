<script lang="ts">
    import { Chess } from 'svelte-chess';
    import '$lib/chessStyle.css';
	import { onMount } from 'svelte';
	import type { Color } from 'chess.js';

    let isGameOver = $state<boolean | undefined>();
    let turn = $state<Color | undefined>();

    let chess: any;
    onMount(() => {
        chess.load("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    })

    function moveListener(event: any) {
        const move = event.detail;
        console.log( `${move.color} played ${move.san}` );
    }

    // function gameOverListener(event: any) {
    //     console.log(`${winner} wins!`);
    // }
</script>

<p class="text-center text-[50px] text-white mt-10"><b>This is LaziBoard</b></p>

<div class="w-[100vw] flex justify-center mt-10">
    <div class="w-[30vw] relative">
        {#if isGameOver}
            <div class="absolute top-0 left-0 w-[100%] h-[100%] bg-black bg-opacity-80 z-50 flex flex-col items-center justify-center">
                <p class="text-white text-3xl">{turn == "b" ? "White" : "Black"} wins!</p>
                <button onclick={() => chess.reset()} class="px-5 py-2 rounded-lg mt-5 bg-blue-600 hover:bg-blue-500 text-white">Reset</button>
            </div>
        {/if}
        <Chess class="cg-paper" on:move={moveListener} bind:this={chess} bind:turn={turn} bind:isGameOver={isGameOver}/>
    </div>
</div>