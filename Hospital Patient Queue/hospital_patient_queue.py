import heapq
from collections import deque
import time

class Patient:
    def __init__(self, name, is_emergency=False):
        self.name = name
        self.is_emergency = is_emergency
        self.arrival_time = time.time()

    def __repr__(self):
        return f"{'[EMERGENCY]' if self.is_emergency else '[REGULAR]'} {self.name}"

class HospitalQueue:
    def __init__(self, avg_service_time=5):
        self.emergency_queue = []   # priority queue (min-heap)
        self.regular_queue = deque()  # normal FIFO queue
        self.avg_service_time = avg_service_time  # in minutes
        self.counter = 0  # to maintain order in heap

    def add_patient(self, patient):
        if patient.is_emergency:
            # Emergency patients get higher priority (earlier served)
            heapq.heappush(self.emergency_queue, (self.counter, patient))
            self.counter += 1
        else:
            self.regular_queue.append(patient)

        wait_time = self.estimate_wait_time()
        print(f"✅ Added {patient}. Estimated wait time: {wait_time} minutes")

    def serve_patient(self):
        if self.emergency_queue:
            _, patient = heapq.heappop(self.emergency_queue)
        elif self.regular_queue:
            patient = self.regular_queue.popleft()
        else:
            print("No patients in queue.")
            return None
        print(f"🚑 Serving {patient}")
        return patient

    def estimate_wait_time(self):
        # Each patient assumed to take avg_service_time
        queue_length = len(self.emergency_queue) + len(self.regular_queue)
        return queue_length * self.avg_service_time


# ------------------ DEMO ------------------
if __name__ == "__main__":
    hospital = HospitalQueue(avg_service_time=10)  # each patient ~10 mins

    hospital.add_patient(Patient("Alice"))              # regular
    hospital.add_patient(Patient("Bob"))                # regular
    hospital.add_patient(Patient("Charlie", True))      # emergency
    hospital.add_patient(Patient("David"))              # regular
    hospital.add_patient(Patient("Eve", True))          # emergency

    print("\n--- Serving patients ---")
    hospital.serve_patient()
    hospital.serve_patient()
    hospital.serve_patient()
    hospital.serve_patient()
    hospital.serve_patient()
    hospital.serve_patient()
