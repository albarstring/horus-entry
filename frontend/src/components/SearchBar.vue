<template>
  <div class="mb-6 flex gap-2">
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      type="text"
      :placeholder="placeholder"
      class="flex-1 px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
    />

    <button
      @click="$emit('search')"
      class="px-6 py-2 bg-black text-white font-bold hover:bg-gray-800 transition-colors border-2 border-black"
    >
      Cari
    </button>

  </div>
</template>

<script setup>
defineProps({
  modelValue: String,
  placeholder: {
    type: String,
    default: 'Cari pengguna...',
  },
})

defineEmits(['update:modelValue', 'search'])
</script>
