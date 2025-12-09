<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white p-8 border-2 border-black max-w-md w-full mx-4">
      <h2 class="text-2xl font-bold mb-4 text-black text-center">Update User</h2>
      <form @submit.prevent="handleSubmit">
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-semibold text-black mb-2">Nama Lengkap</label>
            <input
              v-model="form.nama"
              type="text"
              required
              class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            />
          </div>
          <div>
            <label class="block text-sm font-semibold text-black mb-2">Email</label>
            <input
              v-model="form.email"
              type="email"
              required
              class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            />
          </div>
          <div>
            <label class="block text-sm font-semibold text-black mb-2">Username</label>
            <input
              v-model="form.username"
              type="text"
              required
              class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            />
          </div>
        </div>
        <div class="flex gap-2 mt-6">
          <button
            type="submit"
            :disabled="updating"
            class="flex-1 px-4 py-2 bg-black text-white font-bold hover:bg-gray-800 transition-colors disabled:opacity-50 border-2 border-black"
          >
            {{ updating ? 'Menyimpan...' : 'Update' }}
          </button>
          <button
            type="button"
            @click="$emit('close')"
            class="flex-1 px-4 py-2 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
          >
            Kembali
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  user: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['close', 'update'])

const form = ref({
  username: '',
  nama: '',
  email: ''
})

const updating = ref(false)

watch(() => props.user, (newUser) => {
  if (newUser) {
    form.value = {
      username: newUser.username || '',
      nama: newUser.nama || '',
      email: newUser.email || ''
    }
  }
}, { immediate: true })

const handleSubmit = () => {
  updating.value = true
  emit('update', form.value)
  updating.value = false
}
</script>

