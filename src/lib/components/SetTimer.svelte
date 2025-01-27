<script lang="ts">
	import { timerString } from "$lib/utils/timef";
    import PlusImg from "$lib/assets/svgs/plus.svelte";
    import MinusImg from "$lib/assets/svgs/minus.svelte";

    let { startTime = $bindable<number>(300) } = $props();

    function changeTime(delta: number) {
        startTime += delta;
        if (startTime < 1) startTime = 1;
        if (startTime > 3599) startTime = 3599
    }
</script>

<p class="text-white text-[40px] text-center">{timerString(startTime)}</p>

<div class="flex gap-10">
    <div>
        <p class="text-center text-white">Minutes</p>
        <div class="flex gap-5 w-full justify-center">
            <button 
                onclick={() => changeTime(60)}
                class="bg-green-600 hover:bg-green-500 w-[40px] h-[40px] rounded-lg text-white"
            >
                60
            </button>
            <button 
                onclick={() => changeTime(-60)}
                class="bg-red-600 hover:bg-red-500 w-[40px] h-[40px] rounded-lg text-white"
            >
                60
            </button>
        </div>
    </div>
    
    <div>
        <p class="text-center text-white">Seconds</p>
        <div class="flex gap-5 w-full justify-center">
            <button 
                onclick={() => changeTime(1)}
                class="bg-green-600 hover:bg-green-500 w-[40px] h-[40px] rounded-lg text-white"
            >
                <PlusImg />
            </button>
            <button 
                onclick={() => changeTime(-1)}
                class="bg-red-600 hover:bg-red-500 w-[40px] h-[40px] rounded-lg text-white"
            >
                <MinusImg />
            </button>
        </div>
    </div>
</div>