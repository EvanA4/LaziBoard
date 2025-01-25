<script>
    import {Chess} from 'svelte-chess';
    import '$lib/chessStyle.css';
</script>

<p class="text-center text-[50px] text-white mt-10"><b>This is LaziBoard</b></p>

<div class="w-[100vw] flex justify-center mt-10">
    <div class="w-[30vw]">
        <Chess class="cg-paper"/>
    </div>
</div>