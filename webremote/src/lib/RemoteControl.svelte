<script lang="ts">
  import ControlButton from './ControlButton.svelte';
  import VideoInput from './VideoInput.svelte';

  async function sendCommand(command: string) {
    const response = await fetch('/update', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ commands: command }),
    });

    if (!response.ok) {
      throw new Error('Failed to send command');
    }

    return response.json();
  }
</script>

<div class="w-full max-w-md">
  <div class="bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl p-8 border border-white/20">
    <h1 class="text-4xl font-bold text-white mb-8 text-center">
      Remote Control
    </h1>

    <VideoInput />

    <div class="mt-8 space-y-4">
      <div class="grid grid-cols-2 gap-4">
        <ControlButton
          label="Play / Pause"
          icon="⏯️"
          command="space"
          onSend={sendCommand}
        />

        <ControlButton
          label="Fullscreen"
          icon="⛶"
          command="f"
          onSend={sendCommand}
        />
      </div>
    </div>
  </div>
</div>
