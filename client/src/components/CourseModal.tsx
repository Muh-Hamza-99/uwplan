import { Plus } from "lucide-react";

type Props = {
    modalId: number;
};

const CourseModal = ({ modalId }: Props) => {
  return (
    <>
        <button className="btn btn-ghost btn-circle" onClick={() => (document.getElementById(`course-modal-${modalId}`) as HTMLDialogElement).showModal()}>
            <Plus />
        </button>
        <dialog id={`course-modal-${modalId}`} className="modal modal-bottom sm:modal-middle">
            <div className="modal-box">
                <h3 className="font-bold text-lg">Add Course</h3>
                <p className="py-4">Add a course</p>
                <div className="modal-action">
                    <form method="dialog">
                        <button className="btn">Close</button>
                    </form>
                </div>
            </div>
        </dialog>
    </>
  );
};

export default CourseModal;
