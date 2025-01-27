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


<div class="flex justify-center gap-5 mt-5">
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(600)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                10m
            </button>
            <button 
                onclick={() => changeTime(-600)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                10m
            </button>
        </div>
    </div>
    
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(300)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                5m
            </button>
            <button 
                onclick={() => changeTime(-300)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                5m
            </button>
        </div>
    </div>
</div>

<div class="flex justify-center gap-5 mt-5">
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(60)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                60
            </button>
            <button 
                onclick={() => changeTime(-60)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                60
            </button>
        </div>
    </div>
    
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(30)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                30
            </button>
            <button 
                onclick={() => changeTime(-30)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                30
            </button>
        </div>
    </div>
</div>

<div class="flex justify-center gap-5 mt-5">
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(15)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                15
            </button>
            <button 
                onclick={() => changeTime(-15)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                15
            </button>
        </div>
    </div>
    
    <div>
        <div class="flex gap-0 w-full justify-center rounded-lg overflow-hidden">
            <button 
                onclick={() => changeTime(1)}
                class="bg-green-600 hover:bg-green-500 w-[50px] h-[40px] text-white"
            >
                <PlusImg />
            </button>
            <button 
                onclick={() => changeTime(-1)}
                class="bg-red-600 hover:bg-red-500 w-[50px] h-[40px] text-white"
            >
                <MinusImg />
            </button>
        </div>
    </div>
</div>