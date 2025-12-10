<template>
  <div class="min-h-screen bg-white p-8">
    <div class="max-w-6xl mx-auto">
      <h1 class="text-3xl font-bold mb-6 text-black ">
        DASHBOARD PENGGUNA
      </h1>

      <SearchBar
        v-model="searchQuery"
        @search="searchUsers"
        @reset="loadUsers"
      />

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

      <UserTable
        :users="filteredUsers"
        @edit="openEditModal"
        @delete="confirmDelete"
      />

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
    <UpdateUser
      v-if="showEditModal"
      :user="editForm"
      @close="closeEditModal"
      @update="handleUpdate"
    />

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
import { useRouter } from 'vue-router'
import { useAuth } from '../store/auth'
import api from '../services/api'
import SearchBar from '../components/SearchBar.vue'
import UserTable from '../components/UserTable.vue'
import UpdateUser from '../views/UpdateUser.vue'

const router = useRouter()
const { logout } = useAuth()

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
  searchQuery.value = ''

  try {
    const { data } = await api.getUsers()
    users.value = data
  } catch (err) {
    error.value = err.message || 'Gagal memuat data pengguna'
  } finally {
    loading.value = false
  }
}

const searchUsers = () => {
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

const handleUpdate = async (userData) => {
  error.value = ''
  successMessage.value = ''

  try {
    const { data } = await api.updateUser(editForm.value.id, userData)
    successMessage.value = data.message || 'Data berhasil diperbarui'
    closeEditModal()
    
    setTimeout(async () => {
      await loadUsers()
      setTimeout(() => {
        successMessage.value = ''
      }, 3000)
    }, 100)
  } catch (err) {
    error.value = err.message || 'Gagal memperbarui data'
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
    const { data } = await api.deleteUser(userToDelete.value.id)
    successMessage.value = data.message || 'Pengguna berhasil dihapus'
    closeDeleteModal()
    await loadUsers()
    setTimeout(() => {
      successMessage.value = ''
    }, 3000)
  } catch (err) {
    error.value = err.message || 'Gagal menghapus pengguna'
  } finally {
    deleting.value = false
  }
}

const handleLogout = () => {
  logout()
  router.push('/login')
}

onMounted(() => {
  loadUsers()
})
</script>

