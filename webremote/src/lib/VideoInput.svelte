<script lang="ts">
  let url = '';
  let loading = false;
  let success = false;

  async function handleSubmit() {
    if (loading || !url.trim()) return;

    loading = true;
    success = false;

    try {
      const response = await fetch('/playvideo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error('Failed to play video');
      }

      success = true;
      setTimeout(() => {
        success = false;
      }, 2000);
    } catch (error) {
      console.error('Failed to play video:', error);
    } finally {
      loading = false;
    }
  }
</script>

<div class="space-y-3">
  <label class="block text-white text-sm font-medium mb-2">
    Video URL
  </label>

  <form on:submit|preventDefault={handleSubmit} class="flex gap-3">
    <input
      type="text"
      bind:value={url}
      placeholder="Enter YouTube URL..."
      disabled={loading}
      class="flex-1 bg-white/10 border border-white/30 rounded-xl px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent disabled:opacity-50 disabled:cursor-not-allowed"
    />

    <button
      type="submit"
      disabled={loading || !url.trim()}
      class="relative bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 text-white font-semibold px-6 py-3 rounded-xl shadow-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed min-w-[100px]"
      class:scale-110={success}
      class:animate-pulse={success}
      class:ring-4={success}
      class:ring-green-400={success}
    >
      {#if loading}
        <span class="inline-block animate-spin">⏳</span>
      {:else if success}
        <span>✓</span>
      {:else}
        <span>Play</span>
      {/if}

      {#if success}
        <div class="absolute inset-0 bg-green-500/30 rounded-xl pointer-events-none"></div>
      {/if}
    </button>
  </form>
</div>

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
