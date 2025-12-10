<template>
  <div class="min-h-screen flex items-center justify-center bg-white">
    <div class="w-full max-w-md p-8 border-2 border-black">
      <h1 class="text-3xl font-bold mb-6 text-black text-center">REGISTRASI AKUN</h1>
      
      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label for="nama" class="block text-sm font-semibold text-black mb-2">Nama</label>
          <input
            id="nama"
            v-model="form.nama"
            type="text"
            required
            class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="Masukkan nama lengkap"
          />
        </div>

        <div>
          <label for="username" class="block text-sm font-semibold text-black mb-2">Username</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            required
            class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="Masukkan username"
          />
        </div>

        <div>
          <label for="email" class="block text-sm font-semibold text-black mb-2">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="Masukkan email"
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-semibold text-black mb-2">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            required
            class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="Masukkan password"
          />
        </div>

        <div v-if="error" class="p-3 bg-black text-white text-sm">
          {{ error }}
        </div>

        <div v-if="success" class="p-3 bg-black text-white text-sm">
          {{ success }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 bg-black text-white font-bold hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed border-2 border-black"
        >
          {{ loading ? 'Memproses...' : 'Registrasi' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()

const form = ref({
  nama: '',
  username: '',
  email: '',
  password: ''
})

const loading = ref(false)
const error = ref('')
const success = ref('')

const handleRegister = async () => {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    const { data } = await api.register(form.value)
    success.value = data.message || 'Registrasi berhasil!'
    
    setTimeout(() => {
      router.push('/login')
    }, 2000)
  } catch (err) {
    error.value = err.message || 'Registrasi gagal. Pastikan backend sudah berjalan.'
  } finally {
    loading.value = false
  }
}
</script>

