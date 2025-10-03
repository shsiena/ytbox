<script lang="ts">
  export let label: string;
  export let icon: string;
  export let command: string;
  export let onSend: (command: string) => Promise<any>;

  let loading = false;
  let success = false;

  async function handleClick() {
    if (loading) return;

    loading = true;
    success = false;

    try {
      await onSend(command);
      success = true;
      setTimeout(() => {
        success = false;
      }, 1000);
    } catch (error) {
      console.error('Failed to send command:', error);
    } finally {
      loading = false;
    }
  }
</script>

<button
  on:click={handleClick}
  disabled={loading}
  class="relative group bg-gradient-to-br from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white font-semibold py-6 px-6 rounded-2xl shadow-lg transition-all duration-200 disabled:opacity-70 disabled:cursor-not-allowed flex flex-col items-center justify-center gap-2"
  class:scale-110={success}
  class:animate-pulse={success}
  class:ring-4={success}
  class:ring-green-400={success}
>
  <span class="text-3xl" class:animate-spin={loading}>
    {loading ? '⏳' : icon}
  </span>
  <span class="text-sm">
    {label}
  </span>

  {#if success}
    <div class="absolute inset-0 bg-green-500/30 rounded-2xl pointer-events-none"></div>
  {/if}
</button>

<style>
  @keyframes pulse {
    0%, 100% {
      opacity: 1;
    }
    50% {
      opacity: .8;
    }
  }

  .animate-pulse {
    animation: pulse 0.5s cubic-bezier(0.4, 0, 0.6, 1);
  }
</style>
