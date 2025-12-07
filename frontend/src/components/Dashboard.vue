<template>
  <div class="min-h-screen bg-white p-8">
    <div class="max-w-6xl mx-auto">
      <h1 class="text-3xl font-bold mb-6 text-black border-b-2 border-black pb-2">
        DASHBOARD PENGGUNA
      </h1>

      <!-- Search Bar -->
      <div class="mb-6 flex gap-2">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Cari pengguna..."
          class="flex-1 px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
        />
        <button
          @click="searchUsers"
          class="px-6 py-2 bg-black text-white font-bold hover:bg-gray-800 transition-colors border-2 border-black"
        >
          Cari
        </button>
        <button
          @click="loadUsers"
          class="px-6 py-2 bg-white text-black font-bold hover:bg-gray-100 transition-colors border-2 border-black"
        >
          Reset
        </button>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-8 text-black">
        Memuat data...
      </div>

      <!-- Error State -->
      <div v-if="error" class="p-4 bg-black text-white mb-4">
        {{ error }}
      </div>

      <!-- Success Message -->
      <div v-if="successMessage" class="p-4 bg-black text-white mb-4">
        {{ successMessage }}
      </div>

      <!-- Table -->
      <div class="border-2 border-black overflow-x-auto">
        <table class="w-full border-collapse">
          <thead>
            <tr class="bg-black text-white">
              <th class="border-2 border-black px-4 py-3 text-left font-bold">ID</th>
              <th class="border-2 border-black px-4 py-3 text-left font-bold">Username</th>
              <th class="border-2 border-black px-4 py-3 text-left font-bold">Nama Lengkap</th>
              <th class="border-2 border-black px-4 py-3 text-left font-bold">Email</th>
              <th class="border-2 border-black px-4 py-3 text-left font-bold">Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in filteredUsers" :key="`user-${user.id}`" class="hover:bg-gray-100">
              <td class="border-2 border-black px-4 py-3 text-black font-mono">{{ index + 1 }}</td>
              <td class="border-2 border-black px-4 py-3 text-black">{{ user.username }}</td>
              <td class="border-2 border-black px-4 py-3 text-black">{{ user.nama }}</td>
              <td class="border-2 border-black px-4 py-3 text-black">{{ user.email }}</td>
              <td class="border-2 border-black px-4 py-3">
                <div class="flex gap-2">
                  <button
                    @click="openEditModal(user)"
                    class="px-3 py-1 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
                  >
                    U
                  </button>
                  <button
                    @click="confirmDelete(user)"
                    class="px-3 py-1 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
                  >
                    H
                  </button>
                </div>
              </td>
            </tr>
            <tr v-if="filteredUsers.length === 0">
              <td colspan="5" class="border-2 border-black px-4 py-8 text-center text-black">
                Tidak ada data pengguna
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Logout Button -->
      <div class="mt-6 text-right">
        <button
          @click="handleLogout"
          class="px-6 py-2 bg-black text-white font-bold hover:bg-gray-800 transition-colors border-2 border-black"
        >
          Logout
        </button>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="showEditModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-8 border-2 border-black max-w-md w-full mx-4">
        <h2 class="text-2xl font-bold mb-4 text-black">Edit Pengguna</h2>
        <form @submit.prevent="handleUpdate">
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-semibold text-black mb-2">Username</label>
              <input
                v-model="editForm.username"
                type="text"
                required
                class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-black mb-2">Nama Lengkap</label>
              <input
                v-model="editForm.nama"
                type="text"
                required
                class="w-full px-4 py-2 border-2 border-black bg-white text-black focus:outline-none focus:ring-2 focus:ring-black"
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-black mb-2">Email</label>
              <input
                v-model="editForm.email"
                type="email"
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
              {{ updating ? 'Menyimpan...' : 'Simpan' }}
            </button>
            <button
              type="button"
              @click="closeEditModal"
              class="flex-1 px-4 py-2 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
            >
              Batal
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-8 border-2 border-black max-w-md w-full mx-4">
        <h2 class="text-2xl font-bold mb-4 text-black">Hapus Pengguna</h2>
        <p class="text-black mb-6">
          Apakah kamu yakin ingin menghapus pengguna <strong>{{ userToDelete?.username }}</strong>?
        </p>
        <div class="flex gap-2">
          <button
            @click="handleDelete"
            :disabled="deleting"
            class="flex-1 px-4 py-2 bg-black text-white font-bold hover:bg-gray-800 transition-colors disabled:opacity-50 border-2 border-black"
          >
            {{ deleting ? 'Menghapus...' : 'Hapus' }}
          </button>
          <button
            @click="closeDeleteModal"
            class="flex-1 px-4 py-2 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
          >
            Batal
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const emit = defineEmits(['logout'])

const users = ref([])
const searchQuery = ref('')
const loading = ref(false)
const error = ref('')
const successMessage = ref('')
const showEditModal = ref(false)
const showDeleteModal = ref(false)
const editForm = ref({
  id: null,
  username: '',
  nama: '',
  email: ''
})
const userToDelete = ref(null)
const updating = ref(false)
const deleting = ref(false)

const filteredUsers = computed(() => {
  if (!searchQuery.value.trim()) {
    return users.value
  }
  const query = searchQuery.value.toLowerCase()
  return users.value.filter(user => 
    user.username.toLowerCase().includes(query) ||
    user.nama.toLowerCase().includes(query) ||
    user.email.toLowerCase().includes(query)
  )
})

const loadUsers = async () => {
  loading.value = true
  error.value = ''
  successMessage.value = ''

  try {
    const response = await fetch('http://127.0.0.1:5000/users')
    if (response.ok) {
      users.value = await response.json()
    } else {
      error.value = 'Gagal memuat data pengguna'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan. Pastikan backend sudah berjalan.'
    console.error('Load users error:', err)
  } finally {
    loading.value = false
  }
}

const searchUsers = () => {
  // Filter sudah di-handle oleh computed property
  if (filteredUsers.value.length === 0 && searchQuery.value.trim()) {
    error.value = 'Pengguna tidak ditemukan'
  } else {
    error.value = ''
  }
}

const openEditModal = (user) => {
  editForm.value = {
    id: user.id,
    username: user.username,
    nama: user.nama,
    email: user.email
  }
  showEditModal.value = true
}

const closeEditModal = () => {
  showEditModal.value = false
  editForm.value = {
    id: null,
    username: '',
    nama: '',
    email: ''
  }
}

const handleUpdate = async () => {
  updating.value = true
  error.value = ''
  successMessage.value = ''

  const userId = editForm.value.id // Simpan ID sebelum update

  try {
    const response = await fetch(`http://127.0.0.1:5000/users/${userId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: editForm.value.username,
        nama: editForm.value.nama,
        email: editForm.value.email
      })
    })

    const data = await response.json()

    if (response.ok) {
      successMessage.value = data.message || 'Data berhasil diperbarui'
      closeEditModal()
      
      // Reload data dengan delay kecil untuk memastikan database sudah commit
      setTimeout(async () => {
        await loadUsers()
        setTimeout(() => {
          successMessage.value = ''
        }, 3000)
      }, 100)
    } else {
      error.value = data.message || 'Gagal memperbarui data'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan saat memperbarui data'
    console.error('Update error:', err)
  } finally {
    updating.value = false
  }
}

const confirmDelete = (user) => {
  userToDelete.value = user
  showDeleteModal.value = true
}

const closeDeleteModal = () => {
  showDeleteModal.value = false
  userToDelete.value = null
}

const handleDelete = async () => {
  deleting.value = true
  error.value = ''
  successMessage.value = ''

  try {
    const response = await fetch(`http://127.0.0.1:5000/users/${userToDelete.value.id}`, {
      method: 'DELETE'
    })

    const data = await response.json()

    if (response.ok) {
      successMessage.value = data.message || 'Pengguna berhasil dihapus'
      closeDeleteModal()
      await loadUsers()
      setTimeout(() => {
        successMessage.value = ''
      }, 3000)
    } else {
      error.value = data.message || 'Gagal menghapus pengguna'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan saat menghapus data'
    console.error('Delete error:', err)
  } finally {
    deleting.value = false
  }
}

const handleLogout = () => {
  localStorage.removeItem('token')
  emit('logout')
}

onMounted(() => {
  loadUsers()
})
</script>

