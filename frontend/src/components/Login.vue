<template>
  <div class="min-h-screen flex items-center justify-center bg-white">
    <div class="w-full max-w-md p-8 border-2 border-black">
      <h1 class="text-3xl font-bold mb-6 text-black text-center">Login</h1>
      
      <form @submit.prevent="handleLogin" class="space-y-4">
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

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 bg-black text-white font-bold hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed border-2 border-black"
        >
          {{ loading ? 'Memproses...' : 'Login' }}
        </button>
      </form>

      <p class="mt-6 text-center text-black">
        Belum punya akun?
        <button @click="$emit('switch-to-register')" class="font-bold underline hover:text-gray-700">
          Daftar di sini
        </button>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['switch-to-register', 'login-success'])

const form = ref({
  username: '',
  password: ''
})

const loading = ref(false)
const error = ref('')

const handleLogin = async () => {
  loading.value = true
  error.value = ''

  try {
    const response = await fetch('http://127.0.0.1:5000/users/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: form.value.username,
        password: form.value.password
      })
    })

    const data = await response.json()

    if (response.ok) {
      // Simpan token jika diperlukan
      if (data.token) {
        localStorage.setItem('token', data.token)
      }
      emit('login-success', data)
    } else {
      error.value = data.message || 'Login gagal'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan. Pastikan backend sudah berjalan.'
    console.error('Login error:', err)
  } finally {
    loading.value = false
  }
}
</script>

