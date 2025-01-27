<script lang="ts">
	import { timerString } from "$lib/utils/timef";
    import PlusImg from "$lib/assets/svgs/plus.svelte";
    import MinusImg from "$lib/assets/svgs/minus.svelte";

    let { startTime = $bindable<number>(300) } = $props();

    function changeTime(delta: number) {
        
    }
</script>

<p class="text-white text-[40px] text-center">{timerString(startTime)}</p>

<p class="text-center text-white mt-5">Minutes</p>
<div class="flex gap-5">
    <button 
        onclick={() => startTime += 60}
        class="bg-green-600 hover:bg-green-500 w-[40px] h-[40px] rounded-lg text-white"
    >
        60
    </button>
    <button 
        onclick={() => startTime -= 60}
        class="bg-red-600 hover:bg-red-500 w-[40px] h-[40px] rounded-lg text-white"
    >
        60
    </button>
</div>

<p class="text-center text-white mt-5">Seconds</p>
<div class="flex gap-5">
    <button 
        onclick={() => startTime += 1}
        class="bg-green-600 hover:bg-green-500 w-[40px] h-[40px] rounded-lg text-white"
    >
        <PlusImg />
    </button>
    <button 
        onclick={() => startTime -= 1}
        class="bg-red-600 hover:bg-red-500 w-[40px] h-[40px] rounded-lg text-white"
    >
        <MinusImg />
    </button>
</div>