<template>
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
        <tr v-for="(user, index) in users" :key="`user-${user.id}`" class="hover:bg-gray-100">
          <td class="border-2 border-black px-4 py-3 text-black font-mono">{{ index + 1 }}</td>
          <td class="border-2 border-black px-4 py-3 text-black">{{ user.username }}</td>
          <td class="border-2 border-black px-4 py-3 text-black">{{ user.nama }}</td>
          <td class="border-2 border-black px-4 py-3 text-black">{{ user.email }}</td>
          <td class="border-2 border-black px-4 py-3">
            <div class="flex gap-2">
              <button
                @click="$emit('edit', user)"
                class="px-3 py-1 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
              >
                U
              </button>
              <button
                @click="$emit('delete', user)"
                class="px-3 py-1 bg-white text-black font-bold hover:bg-gray-200 transition-colors border-2 border-black"
              >
                H
              </button>
            </div>
          </td>
        </tr>
        <tr v-if="users.length === 0">
          <td colspan="5" class="border-2 border-black px-4 py-8 text-center text-black">
            Tidak ada data pengguna
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
defineProps({
  users: {
    type: Array,
    required: true,
    default: () => [],
  },
})

defineEmits(['edit', 'delete'])
</script>

